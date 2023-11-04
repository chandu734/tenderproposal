from django.db import models

class ProposalSection(models.Model):
    section_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.section_name

class TenderProposal(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    proposal_summary = models.TextField()
    project_planning = models.ManyToManyField(ProposalSection, related_name='project_planning_sections')
    financing = models.ManyToManyField(ProposalSection, related_name='financing_sections')
    additional_sections = models.ManyToManyField(ProposalSection, related_name='additional_sections')

    def __str__(self):
        return self.title
