from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy, Benchmark
from .forms import InvestmentGuidelineForm, InvestmentGuidelineOptionsForm, InlineFormSetField, IGOptionsFormSet, BenchmarkForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from django.urls import reverse_lazy


@login_required
def investmentguidelines_list(request):
    igs = InvestmentGuideline.objects.order_by('portfolio_code')
    return render(request, 'core/investmentguideline/list.html', {'igs': igs})

@login_required
def investmentguidelines_detail(request, pk):
    ig = get_object_or_404(InvestmentGuideline, pk=pk)
    ig_opts = InvestmentGuidelineOptions.objects.filter(investmentguideline_id=pk)
    return render(request, 'core/investmentguideline/detail.html', {'ig': ig, 'ig_opts': ig_opts})

@login_required
def benchmark_detail(request, pk):
    bm = get_object_or_404(Benchmark, pk=pk)
    return render(request, 'core/benchmark/detail.html', {'bm': bm})



class InvestmentGuidelineCreate(CreateView):
    model = InvestmentGuideline
    template_name = 'core/investmentguideline/create.html'
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
        return reverse_lazy('core:ig_create', kwargs={'pk': self.object.pk})


@login_required
class InvestmentGuidelineUpdate(CreateView):
    model = InvestmentGuideline
    template_name = 'core/edit.html'
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
        return reverse_lazy('core:ig_detail', kwargs={'pk': self.object.pk})



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
    return render(request, 'core/edit.html', {'form': form})

@login_required
def benchmark_edit(request, pk):
    bm = get_object_or_404(Benchmark, pk=pk)
    if (request.method == 'POST'):
        form = BenchmarkForm(request.POST, instance=bm)
        if (form.is_valid()):
            bm = form.save(commit=False)
            bm.updated_by = request.user
            bm.save()
            return redirect('bm_detail', pk=bm.pk)
    else:
        form = BenchmarkForm(instance=bm)
    return render(request, 'core/benchmark/edit.html', {'form': form})



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
    return render(request, 'core/edit.html', {'form': form})



class BenchmarkCreate(CreateView):
    model = Benchmark
    template_name = 'core/benchmark/edit.html'
    form_class = BenchmarkForm


    def get_success_url(self):
        return reverse_lazy('core:bm_list', kwargs={})


@login_required
def indexview(request):
    return render(request, 'core/index.html')



@login_required
def benchmarks_list(request):
    bms = Benchmark.objects.order_by('benchmark_name')
    return render(request, 'core/benchmark/list.html', {'bms': bms})


@login_required
def benchmark_new(request):
    if request.method == "POST":
        form = BenchmarkForm(request.POST)
        if form.is_valid():
            bm = form.save(commit=False)
            bm.created_by = request.user
            bm.updated_by = request.user
            bm.save()
            return redirect('bm_list')
    else:
        form = BenchmarkForm()
    return render(request, 'core/benchmark/edit.html', {'form': form})