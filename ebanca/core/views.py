from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, RedirectView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from core.forms import ClientForm, SignInForm
from core.models import Client, User, CreditCard, Account
from core import utils


class ClientListView(TemplateView):

    # model = Client
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['users'] = User.objects.all()
        return context


class SignUpView(FormView):

    form_class = ClientForm
    template_name = 'signup.html'
    success_url = '/'

    @transaction.atomic
    def form_valid(self, form):

        # save client
        form.save()
        # generate data
        num_card = utils.generateNumCard()
        num_pin = utils.generateNumPin()
        getClient = form.cleaned_data['document_number']
        # add user
        user = User(username=num_card, client=Client.objects.get(document_number=getClient))
        user.set_password(num_pin)
        user.save()
        # add card
        card = CreditCard(num_card=num_card, num_pin=num_pin,
                            expiration_date=utils.generateExpDate(), num_cvv=utils.generateNumCvv())
        card.save()
        # add account
        account = Account(
            num_account=utils.generateNumAccount(), client=Client.objects.get(document_number=getClient), card=CreditCard.objects.get(num_card=num_card))
        account.save()
        return super(SignUpView, self).form_valid(form)


class SignInView(FormView):

    form_class = SignInForm
    template_name = 'signin.html'
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['num_card'], password=form.cleaned_data['num_pin'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(SignInView, self).form_valid(form)


class LogoutView(RedirectView):

    url = '/signin/'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)
