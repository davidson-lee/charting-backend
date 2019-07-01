import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from stock.models import Corporation, Trades

class CorporationType(DjangoObjectType):
    class Meta:
        model = Corporation

class TradesType(DjangoObjectType):
    class Meta:
        model = Trades

class Query(ObjectType):
    corporation = graphene.Field(CorporationType, id=graphene.Int())
    movie = graphene.Field(TradesType, id=graphene.Int())
    corporations = graphene.List(CorporationType)
    trades = graphene.List(TradesType)

    def resolve_corporation(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Corporation.objects.get(id=id)
        
        return None
    
    def resolve_trade(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Trades.objects.get(id=id)
        
        return None
    
    def resolve_corporations(self, info, **kwargs):
        return Corporation.objects.all()
    
    def resolve_trades(self, info, **kwargs):
        return Trades.objects.all()

schema = graphene.Schema(query=Query)