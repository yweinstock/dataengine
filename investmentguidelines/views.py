from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy
from .forms import InvestmentGuidelineForm, InvestmentGuidelineOptionsForm
from django.contrib.auth.decorators import login_required
# from django.conf import settings


@login_required
def investmentguidelines_list(request):
    igs = InvestmentGuideline.objects.order_by('portfolio_code')
    return render(request, 'investmentguidelines/ig_list.html', {'igs': igs})

@login_required
def investmentguidelines_detail(request, pk):
    ig = get_object_or_404(InvestmentGuideline, pk=pk)
    ig_opts = InvestmentGuidelineOptions.objects.filter(investmentguideline_id=pk)
    return render(request, 'investmentguidelines/ig_detail.html', {'ig': ig, 'ig_opts': ig_opts})

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
