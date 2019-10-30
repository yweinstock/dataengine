from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy
from .forms import InvestmentGuidelineForm, InvestmentGuidelineOptionsForm, InlineFormSetField, IGOptionsFormSet
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from django.urls import reverse_lazy


@login_required
def investmentguidelines_list(request):
    igs = InvestmentGuideline.objects.order_by('portfolio_code')
    return render(request, 'investmentguidelines/ig_list.html', {'igs': igs})

@login_required
def investmentguidelines_detail(request, pk):
    ig = get_object_or_404(InvestmentGuideline, pk=pk)
    ig_opts = InvestmentGuidelineOptions.objects.filter(investmentguideline_id=pk)
    return render(request, 'investmentguidelines/ig_detail.html', {'ig': ig, 'ig_opts': ig_opts})

class InvestmentGuidelineCreate(CreateView):
    model = InvestmentGuideline
    template_name = 'investmentguidelines/ig_create.html'
    form_class = InvestmentGuidelineForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(InvestmentGuidelineCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['investment_guideline_options'] = IGOptionsFormSet(self.request.POST)
        else:
            data['investment_guideline_options'] = IGOptionsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        investment_guideline_options = context['investment_guideline_options']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if investment_guideline_options.is_valid():
                investment_guideline_options.instance = self.object
                investment_guideline_options.save()
        return super(InvestmentGuidelineCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('investmentguidelines:ig_create', kwargs={'pk': self.object.pk})



class InvestmentGuidelineUpdate(CreateView):
    model = InvestmentGuideline
    template_name = 'investmentguidelines/ig_edit.html'
    form_class = InvestmentGuidelineForm
    success_url = None


    def get_context_data(self, **kwargs):
        data = super(InvestmentGuidelineUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['investment_guideline_options'] = IGOptionsFormSet(self.request.POST, instance=self.object)
        else:
            data['investment_guideline_options'] = IGOptionsFormSet(instance=self.object)
        return data


    def form_valid(self, form):
        context = self.get_context_date()
        investment_guideline_options = context['investment_guideline_options']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if investment_guideline_options.is_valid():
                investment_guideline_options.instance = self.object
                investment_guideline_options.save()
        return super(InvestmentGuidelineUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('investmentguidelines:ig_detail', kwargs={'pk': self.object.pk})



@login_required
def investmentguidelines_new(request):
    if request.method == "POST":
        form = InvestmentGuidelineForm(request.POST)

        if form.is_valid():
            ig = form.save(commit=False)
            ig.created_by = request.user
            ig.updated_by = request.user
            ig.save()
            strategies = request.POST.getlist('strategies')
            for s_id in strategies:
                s = Strategy.objects.get(pk=s_id)
                # todo add logic to check if we are saving a valid strategy
                ig_opt = InvestmentGuidelineOptions.objects.create(
                    investmentguideline=ig,
                    strategy=s,
                    created_by = request.user,
                    updated_by = request.user
                )
                ig_opt.save()
            return redirect('ig_detail', pk=ig.pk)
    else:
        form = InvestmentGuidelineForm()
    return render(request, 'investmentguidelines/ig_edit.html', {'form': form})






@login_required
def investmentguidelines_edit(request, pk):
    ig = get_object_or_404(InvestmentGuideline, pk=pk)
    if (request.method == 'POST'):
        form = InvestmentGuidelineForm(request.POST, instance=ig)
        if form.is_valid():
            ig = form.save(commit=False)
            ig.updated_by = request.user
            ig.save()
            strategies = request.POST.getlist('strategies')
            # current_ig_opts = InvestmentGuidelineOptions.objects.filter(investmentguideline=ig)
            for s_id in strategies:
                s = Strategy.objects.get(pk=s_id)
                # todo add logic to check if we are saving a valid strategy
                ig_opt, created = InvestmentGuidelineOptions.objects.get_or_create(investmentguideline=ig,strategy=s)
                if (created):
                    ig_opt.created_by = request.user
                    ig_opt.updated_by = request.user
                    ig_opt.save()
                else:
                    ig_opt.updated_by = request.user
                    ig_opt.save()
            ig_opts_del = InvestmentGuidelineOptions.objects.filter(investmentguideline=ig).exclude(
                strategy_id__in=strategies)
            ig_opts_del.delete()
            return redirect('ig_detail', pk=ig.pk)
    else:
        form = InvestmentGuidelineForm(instance=ig)
    return render(request, 'investmentguidelines/ig_edit.html', {'form': form})
