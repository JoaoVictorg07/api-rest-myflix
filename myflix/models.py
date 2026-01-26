from django.db import models

'''
    id 
    nome
    email
    cpf (maximo 11 caracteres)
    data de nascimento
    numero de telefone(maximo de 14 caracteres)
'''

class user(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

''''
    id 
    codigo do stream (maximode 10 caracteres)
    descrição
    categoria (filme, série e documentario)
'''

class stream(models.Model):
    CATEGORIA = (
        ('F','Filme'),
        ('S', 'Série'),
        ('D', 'Documentario'),
    )
    codigo = models.IntegerField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False,)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, default='F')

    def __str__(self):
        return self.codigo