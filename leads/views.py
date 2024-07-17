from django.shortcuts import render , redirect, reverse
from .models import Lead
from django.core.mail import send_mail
from .forms import LeadWalaForm, CustomUserCreationForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView, TemplateView, View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

class LogoutView( View):
    def get(self, request):
        logout(request)
        return redirect('login')
class SignupView(CreateView):
     template_name= 'registration/signup.html'
     form_class = CustomUserCreationForm

     def get_success_url(self) :
            return reverse("login")

class LandingView(TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    queryset =  Lead.objects.all()
    context_object_name = 'lead'

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
class LeadCreateView(LoginRequiredMixin,CreateView):
        template_name = 'create.html'
        form_class = LeadWalaForm
        def get_success_url(self) :
            return reverse("getlead")
        def form_valid(self, form):
             send_mail(
                  subject="Lead created",
                  message= "New lead created",
                  from_email="eb20103109.raohammadali@gmail.com",
                  recipient_list=["d@gmail.com"]
             )

             return super(LeadCreateView, self).form_valid(form)
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name:'leads/lead_form.html'
    queryset = Lead.objects.all()
    form_class = LeadWalaForm
    def get_success_url(self) :
            return reverse("getlead") 
class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name:'leads/lead_confirm_delete.html'
    queryset = Lead.objects.all()
  
    def get_success_url(self) :
            return reverse("getlead") 


# def add_lead(request):
#     if request.method == 'POST':
#         form = LeadWalaForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
            
#             print("Lead created successfully")
#             return redirect("/api/")  # Redirect to desired URL after successful form submission
#     else:
#         form = LeadWalaForm()
    
#     return render(request, 'create.html', {'form': form})
# # Create your views here.
# # def add_lead(request):
# #     if request.method == 'POST':
# #         form = LeadWalaForm(request.POST, request.FILES)

# #         if form.is_valid():
# #             firstname = form.cleaned_data['firstname']
# #             lastname = form.cleaned_data['lastname']
# #             age = form.cleaned_data['age']
# #             phoned = form.cleaned_data.get('phoned', False)  # Use get() with a default value for optional fields like checkboxes
# #             source = form.cleaned_data['source']
# #             profilephoto = form.cleaned_data['profilephoto']
# #             special_files = form.cleaned_data['special_files']
# #             agent = form.cleaned_data['agent']
            
# #             # Create Lead object
# #             Lead.objects.create(
# #                 firstname=firstname,
# #                 lastname=lastname,
# #                 age=age,
# #                 phoned=phoned,
# #                 source=source,
# #                 profilephoto=profilephoto,
# #                 special_files=special_files,
# #                 agent=agent
# #             )
            
# #             print("Lead created successfully")
# #             return redirect("/api/")  # Redirect to desired URL after successful form submission
# #     else:
# #         form = LeadWalaForm()
    
# #     return render(request, 'create.html', {'form': form})
# def get_lead(request):
#     lead = Lead.objects.all().values
#     return render(request, 'home.html', {'lead': lead})
# def detail_lead(request, pk):
#     lead = Lead.objects.filter(id = pk).values()
#     return render(request, 'detail.html', {'lead': lead})
# # def update_lead(request, pk):
# #     lead = Lead.objects.get(id = pk)
# #     form = LeadWalaForm()
# #     if request.method == 'POST':
# #         form = LeadWalaForm(request.POST)
# #         if form.is_valid():
# #             lead.firstname = form.cleaned_data['firstname']
# #             lead.lastname = form.cleaned_data['lastname']
# #             lead.age = form.cleaned_data['age']
# #             lead.phoned = form.cleaned_data.get('phoned', False)  # Use get() with a default value for optional fields like checkboxes
# #             lead.source = form.cleaned_data['source']
# #             lead.profilephoto = form.cleaned_data['profilephoto']
# #             lead.special_files = form.cleaned_data['special_files']
# #             lead.agent = form.cleaned_data['agent']
# #             lead.save()
# #             return redirect("/api/")

# #     return render(request, 'update.html',{'form': form})
# def update_lead(request, pk):
#     lead = Lead.objects.get(id = pk)
#     form = LeadWalaForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadWalaForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/api/")

#     return render(request, 'update.html',{'form': form})
# def delete_lead(request, pk):
#     lead = Lead.objects.get(id = pk)
#     lead.delete()
#     return redirect('/api/')

# def  landing_page(request):
#     return render(request, 'landing.html')