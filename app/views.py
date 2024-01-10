from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache,cache_control
from django.utils.decorators import method_decorator
from .models import ShortCourse
from .forms import ShortCourseForm



@method_decorator(cache_control(no_cache=True, no_store=True, must_revalidate=True), name='dispatch')
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html')



@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')




@method_decorator(cache_control(no_cache=True, no_store=True, must_revalidate=True), name='dispatch')
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        return redirect('login')



class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        return redirect('login')

    def post(self, request):
        '''
        user can change his profile
        '''
        user = request.user
        current_password = request.POST.get('current_password')
        if user.check_password(current_password):
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                # after change the password user object is changed os it is not possible to login with the old session id
                logout(request) 
                user.set_password(new_password)
                user.save()
                # user need to logged in with the new password
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'profile.html', {'error': 'Passwords do not match'})
        else:
            return render(request, 'profile.html', {'error': 'Current password is incorrect'})



    

def shortCourseListView(request):
    if request.user.is_authenticated:
        course_list = ShortCourse.objects.all()
        for x in course_list:
            print(x.status)
        return render(request,'short_course_view.html',context={'course_list': course_list})
    return redirect('login')




class CreateCourseView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'short-course-create.html')
        return redirect('login')
    
    
    def post(self, request):
        form = ShortCourseForm(request.POST, request.FILES)
        if form.is_valid():
            ShortCourse.objects.create(
                title = request.POST.get("title"),
                subtitle = request.POST.get("subtitle"),
                discription = request.POST.get("discription"),
                amount = request.POST.get("amount"),
                status = request.POST.get("status"),
                image = request.FILES.get("image"),
            )
            return redirect('courses')
        return redirect('addcourses')



def deleteCourseView(request,id):
    if request.user.is_authenticated:
        ShortCourse.objects.get(id=id).delete()
        return redirect('courses')
    return redirect('login')




