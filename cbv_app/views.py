from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from http import HTTPStatus
# Create your views here.


class NewView(View):
    def get(self, request): # 200
        print("in get method")
        return HttpResponse("success")
    
    def post(self,request):          #201
        data = request.POST
        name = data.get("name")
        age = data.get("age")

        print("in post method")
        return HttpResponse('post response', status=HTTPStatus.CREATED)
    
    # put : update karna old data add karna padta hai
    # patch:partial data update karna hota hai single data add kar sakte ho
    # delete:204

from django.views.generic.edit import CreateView
from cbv_app.models import Employee

class EmployeeCreate(CreateView):
      model = Employee
      fields = "__all__"
      success_url = "http://127.0.0.1:8000/cbv/emp-create"

      def form_valid(self,form):
          print("saving the data in database")
          return super().form_valid(form)

from django.views.generic.list import ListView

class EmployeeList(ListView):                 # object_list
    model = Employee
    context_object_name = "all_employees"
    ordering = "email"
    # queryset = Employee.objects.filter(is_active =1)

from django.views.generic.detail import DetailView

class EmployeeDetail(DetailView):
    model = Employee
    context_object_name = "single_employee"

    
    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            return "No Data"
        return obj

    def get(self, request, *args, **kwargs):                  # overriding method
        self.object = self.get_object()
        print(type(self.object))
        if type(self.object) == str:
            return HttpResponse("No Data found")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    

    from django.views.generic.edit import DeleteView
    class EmployeeDeleteView(DeleteView):
        model = Employee



        
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        # self.object.is_active = 0            # soft delete
        # self.object.save()
        return HttpResponseRedirect(success_url)


