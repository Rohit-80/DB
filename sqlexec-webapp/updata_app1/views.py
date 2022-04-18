from django.shortcuts import render
from updata_app1.forms import QueryForm
import mysql.connector


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)

        if form.is_valid(): 
            mydb = mysql.connector.connect(
                 host="localhost",
                 user="test",
                 password="ok_1234",
                 database="mytestdb"
               )
            query = form.cleaned_data['query'] 
            mycursor = mydb.cursor()
            lists = query.split()
            print(lists[0])


            try : 
             mycursor.execute(query)  
             if(lists[0] != 'select'):
              mydb.commit()
            
             myresult = mycursor.fetchall()
             row = sequence = mycursor.column_names  
             context = {
                'res' : myresult,
                'dec' : row,
                'form' : form
               }
             return render(request, 'updata_app1/home.html', context)
            except :
                st = "INVALID Query "
                context = {
                    'ok' :  st
                }
                return render(request, 'updata_app1/home.html', context)
             # cursor.execute(mySql_insert_query)
            

            
    else:
        form = QueryForm()

    context = {
        'form': form,
    }
    return render(request, 'updata_app1/home.html', context)
