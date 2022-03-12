from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endorsement, Comment
from .form import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, QuestionForm


# Create your views here.


def home_page(request):
    projects = Project.objects.all()
    skills = Skill.objects.filter(body='')
    detailed_skills = Skill.objects.exclude(body='')

    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message is successfully sent.')

    endorsements = Endorsement.objects.filter(approved=True)

    context = {
        'projects': projects,
        'skills': skills,
        'detailed_skills': detailed_skills,
        'form': form,
        'endorsements': endorsements,
               }
    return render(request, 'base/home.html', context=context)


def project_page(request, pk):
    project = Project.objects.get(id=pk)
    comments = project.comment_set.all().order_by('-created')
    count = project.comment_set.count()

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            form = CommentForm()
            messages.success(request, 'Comment submit successfully.')

    context = {
        'project': project,
        'comments': comments,
        'count': count,
        'form': form,
    }
    return render(request, 'base/project.html', context=context)


def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/project_form.html', context=context)


def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'base/project_form.html', context=context)


def inbox(request):
    inbox = Message.objects.all().order_by('is_read', '-created')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {
        'inbox': inbox,
        'unreadCount': unreadCount,
    }
    return render(request, 'base/inbox.html', context=context)


def message_detail(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {
        'message': message,
    }
    return render(request, 'base/message.html', context=context)


def add_skill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added a skill.')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'base/skill_form.html', context=context)


def add_endorsement(request):
    form = EndorsementForm()
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added an endorsement.')
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'base/endorsement_form.html', context=context)


def donation_page(request):
    return render(request, 'base/donation.html')


def chart_page(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        form.save()
        messages.success(
            request, 'Thank you your vote!')
        return redirect('chart')
    context = {
        'form': form,
    }
    return render(request, 'base/chart.html', context=context)
