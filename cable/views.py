
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ResidencDimens
from .models import Project
from .forms import ResidencDimensForm
from .forms import ProjectForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import main
from django import db


def home(request):
    #db.reset_queries()
    project = Project.objects.all()

    return render(request, 'cable/home.html', {'project': project})

def taskList(request, id):

    read_project = get_object_or_404(Project, pk=id)

    project = main.read_sql_filter(id)
    name_project = project['project'][0]
    
    task = ResidencDimens.objects.filter(projeto_id=read_project).order_by('-local')
    project = Project.objects.all()

    return render(request, 'cable/lista-circuitos.html', {'task': task, 'name_project': name_project, 'project': project})


def newTask(request):

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------
 
            t_va = float(task.total_va)

            task.corrente_a = (float(task.total_va) / t_va)
            #--------------------------------------------------
            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]

            calc = ((((float(queda_tensao) * float(task.corrente_a)) * float(task.comprimento)) / (1000) / t_va))

            task.queda_tensao_ckt = calc * 100
            
            if (float(task.queda_tensao_perm) / 100)< task.queda_tensao_ckt:
                task.queda_tensao_test = 'OK'
            else:
                task.queda_tensao_test = 'NÃO'
            #--------------------------------------------------
            corr = task.sessao_condutor
            test = main.read_sql_corr(corr)
            corrente = test['capacidade_conducao'][0]

            if corrente > float(task.corrente_a):
                task.capacidade_corrente = 'OK'
            else:
                task.capacidade_corrente = 'NÀO'
            #--------------------------------------------------
            dj = task.corrente_nominal
            test = main.read_sql_dj(dj)
            djj = int(test['dj'][0])

            if djj > (float(task.corrente_a) * 1.1):
                task.verifica_dj = 'OK'
            else:
                task.verifica_dj = 'NÀO'

            #--------------------------------------------------
            id_x = task.projeto
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #--------------------------------------------------

            task.save()

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


def editTask(request, id):

    task = get_object_or_404(ResidencDimens, pk=id)
    form = ResidencDimensForm(instance=task)

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST, instance=task)

        if form.is_valid():

            task.save()

            #---------------------------------------------
            id_x = task.projeto
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #---------------------------------------------

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

        else:
            return render(request, 'cable/edit-task.html', {'form': form, 'task': task})

    else:
        return render(request, 'cable/edit-task.html', {'form': form, 'task': task})


def deleteTask(request, id):
    task = get_object_or_404(ResidencDimens, pk=id)

    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    #--------------------------------------------------
    id_x = task.projeto
    test = main.read_sql_filter_id(id_x)
    id_project = int(test['id'][0])
    #--------------------------------------------------

    link = '/tasklist'
    url = '{}/{}'.format(link, id_project)
    return redirect(url)

#------------------------------

def newProject(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            
            project.save()

            return redirect('/')

    else:
        form = ProjectForm()
        return render(request, 'cable/add-project.html', {'form': form})


def editProject(request, id):
    project = get_object_or_404(Project, pk=id)

    form = ProjectForm(instance=project)

    print('\n\n\n')
    print(form )
    print('\n\n\n')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():

            project.save()

            return redirect('/')

        else:
            return render(request, 'cable/edit-project.html', {'form': form, 'project': project})

    else:
        return render(request, 'cable/edit-project.html', {'form': form, 'project': project})


def deleteProject(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')


def test(request):

    task = ResidencDimens.objects.all()

    return render(request, 'cable/test.html', {'task': task})


def helloworld(request):
    return HttpResponse('Hello World!')


