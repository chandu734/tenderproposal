from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TenderProposal, ProposalSection


def create_proposal(request):
    if request.method == 'POST':
        proposal = TenderProposal(
            title=request.POST.get('title'),
            company_name=request.POST.get('company_name'),
            contact_name=request.POST.get('contact_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            proposal_summary=request.POST.get('proposal_summary')
        )
        proposal.save()
        return HttpResponse("Proposal created successfully")
    return render(request,'templates/create_proposal.html')


def edit_proposal(request, proposal_id):
    proposal = get_object_or_404(TenderProposal, pk=proposal_id)
    if request.method == 'POST':
        proposal.title = request.POST.get('title')
        proposal.company_name = request.POST.get('company_name')
        proposal.contact_name = request.POST.get('contact_name')
        proposal.email = request.POST.get('email')
        proposal.phone_number = request.POST.get('phone_number')
        proposal.proposal_summary = request.POST.get('proposal_summary')
        proposal.save()
        return HttpResponse("Proposal updated successfully")
    return render(request,'templates/edit_proposal.html', {'proposal': proposal})

def manage_proposals(request):
    proposals = TenderProposal.objects.all()
    return render(request,'templates/manage_proposals.html', {'proposals': proposals})
