# app/schema.py
import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from django.contrib.auth import authenticate, login
from .models import User, Account, Contact, Address


class UserType(DjangoObjectType):
  class Meta:
    model = User


class AccountType(DjangoObjectType):
  class Meta:
    model = Account


class ContactType(DjangoObjectType):
  class Meta:
    model = Contact


class AddressType(DjangoObjectType):
  class Meta:
    model = Address


class AddressInput(graphene.InputObjectType):
  street = graphene.String()
  city = graphene.String()
  state = graphene.String()
  country = graphene.String()
  zip_code = graphene.String()


class UserInput(graphene.InputObjectType):
  first_name = graphene.String()
  last_name = graphene.String()
  username = graphene.String()
  password = graphene.String()
  department = graphene.String()
  title = graphene.String()
  role = graphene.String()
  email = graphene.String()
  email_signature = graphene.String()
  phone = graphene.String()
  mobile = graphene.String()
  home_phone = graphene.String()
  manager = graphene.ID()
  password_reset_attempt = graphene.Int()
  password_reset_lockout_date = graphene.DateTime()
  


class AccountInput(graphene.InputObjectType):
  first_name = graphene.String()
  last_name = graphene.String()
  billing_address = graphene.ID()
  phone = graphene.String()
  is_active = graphene.Boolean()
  type = graphene.String()


class ContactInput(graphene.InputObjectType):
  account = graphene.ID(required=True)
  first_name = graphene.String()
  last_name = graphene.String()
  birthdate = graphene.Date()
  email = graphene.String()
  email_opt_out = graphene.Boolean()
  home_phone = graphene.String()
  mailing_address = graphene.ID()
  mobile = graphene.String()


class CreateAddress(graphene.Mutation):
  class Arguments:
    input = AddressInput(required=True)

  ok = graphene.Boolean()
  address = graphene.Field(AddressType)

  def mutate(root, info, input):
    address = Address(**input)
    address.save()
    return CreateAddress(address=address, ok=True)


class CreateUser(graphene.Mutation):
  class Arguments:
    input = UserInput(required=True)

  ok = graphene.Boolean()
  user = graphene.Field(UserType)

  def mutate(root, info, input):
    password = input.pop("password")
    manager_id = input.pop("manager", None)
    manager = None
    if manager_id:
        manager = User.objects.get(pk=manager_id)
    user = User(manager=manager, **input)
    user.set_password(password)
    user.save()
    return CreateUser(user=user, ok=True)


class CreateAccount(graphene.Mutation):
  class Arguments:
    input = AccountInput(required=True)

  ok = graphene.Boolean()
  account = graphene.Field(AccountType)

  def mutate(root, info, input):
    address = Address.objects.get(pk=input.pop("billing_address"))
    account = Account(billing_address=address, **input)
    account.save()
    return CreateAccount(account=account, ok=True)


class CreateContact(graphene.Mutation):
  class Arguments:
    input = ContactInput(required=True)

  ok = graphene.Boolean()
  contact = graphene.Field(ContactType)

  def mutate(root, info, input):
    mailing_address = Address.objects.get(pk=input.pop("mailing_address"))
    account = Account.objects.get(pk=input.pop("account"))
    contact = Contact(account=account, mailing_address=mailing_address, **input)
    contact.save()
    return CreateContact(contact=contact, ok=True)


class Login(graphene.Mutation):
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  user = graphene.Field(UserType)
  token = graphene.String()
  error_message = graphene.String()
  access = graphene.String()
  refresh = graphene.String()

  @staticmethod
  def mutate(root, info, username, password):
    print("mutation started")
    user = authenticate(info.context, username=username, password=password)
    print("authenticated")
    if user is not None:
      print(f'auth_result read')
      return Login(user=user, error_message=None)
    else:
      return Login(user=None, error_message="Invalid username or password.")


class Mutation(graphene.ObjectType):
  login = Login.Field()
  create_user = CreateUser.Field()
  create_address = CreateAddress.Field()
  create_account = CreateAccount.Field()
  create_contact = CreateContact.Field()


class Query(graphene.ObjectType):
  users = graphene.List(UserType, role=graphene.String())
  accounts = graphene.List(AccountType)
  contacts = graphene.List(ContactType)

  user = graphene.Field(UserType, id=graphene.ID())

  def resolve_user(root, info, id=id):
    try:
      return User.objects.get(pk=id)
    except User.DoesNotExist:
      return None

  def resolve_users(root, info, role=None):
    if role is not None:
      return User.objects.filter(role=role)
    else:
      return User.objects.all()

  def resolve_accounts(root, info):
    return Account.objects.all()

  def resolve_contacts(root, info):
    return Contact.objects.all()

  address = graphene.Field(AddressType, id=graphene.ID())

  def resolve_address(root, info, id):
    try:
      return Address.objects.get(pk=id)
    except Address.DoesNotExist:
      return None


schema = graphene.Schema(query=Query, mutation=Mutation)
