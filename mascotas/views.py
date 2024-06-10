from django.shortcuts import render, redirect
#from django.http import HttpResponse

mascotas= [{'id':1,
				'nombre':'Jackito',
				'especie': 'tortuga',
				'vacunas': ['octuple'],
				'url':'https://www.tortugaswiki.com/Imagenes/tortugas-terrestres.jpg'
				
			},
				{'id':2,
				'nombre':'Spike',
				'especie': 'perro',
				'vacunas': ['octuple ', 'antirrabica'],
				'url':'https://i.kym-cdn.com/photos/images/original/001/354/305/963.gif'
				
			},
			{'id':3,
				'nombre':'Sulema',
				'especie': 'gato',
				'vacunas': ['octuple ', 'antirrabica', 'antibioticos'],
				'url':'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGFzeWNvYzd0dDZocWY3M3hmeXg5bmtvYmZ6ZWI2ZXFqbHo5ZTBjMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FgNmKgaqixS3m/giphy.webp'
			}
]
# Create your views here.
def paginaMascotas(req):
	
	#return HttpResponse('Pagina de las mascotas')
	context = {
			
			
		
		
		'titulo': 'Esta es la página de las Mascotas;)',
		'esAdmin': True,
		'nombre': 'Carlos Moreno',
		'mascotas': mascotas,
		
	}
	return render(req,'mascotas.html', context)

def detalleMascotas(req, id):
	id=int(id)
	masc_encontrada = None
	for masc in mascotas:
		if masc['id'] == id:
			masc_encontrada = masc
			break
	context = {
		'mascota': masc_encontrada
	}
	return render(req,'detalle.html', context)

def crear_mascota(req):
    print(req.POST['nombre'])
    print(req.POST['especie'])
    return redirect('/pets')