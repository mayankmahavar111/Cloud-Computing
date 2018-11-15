from django import forms
from .models import General,Hosts, Costs


AllocationPolicy =(
    (1,"SingleThreshold"),
    (2,"MultiThreshold"),
)

OS =(
    (1 , "Operating System 1"),
    (2 , "Operating System 2")
)

Hypervisor =(
    (1 , "Hypervisor System 1"),
    (2 , "Hypervisor System 2")
)

VMMigrations=(
    (1 , "Vmmigration 1"),
    (2 , "VMmigration 2")
)


class GeneralForm(forms.Form):
    key = forms.IntegerField(required=True , label='Key' , min_value=0)
    AllocationPolicy = forms.ChoiceField(required=True , label='AllocationPolicy', choices=AllocationPolicy)
    os = forms.ChoiceField(required=True, label='OS' , choices=OS)
    Hypervisor = forms.CharField(required=True,label='Hypervisor')
    SchedulingInterval = forms.CharField(required=True,label='SchedulingInterval')
    UpperThreshold = forms.FloatField(required=True,label='UpperThreshold' , min_value=0)
    LowerThreshold = forms.FloatField(required=True , label='lowerThreshold' ,min_value=0)
    VMmigrations = forms.ChoiceField(required=True , label='VMmigrations' , choices=VMMigrations)
    MonitoringInterval = forms.IntegerField(required=True ,label='MonitoringInterval' , min_value=0)

    class Meta:
        model = General
        fields=(
            'key',
            'AllocationPolicy',
            'os',
            'Hypervisor',
            'SchedulingInterval',
            'UpperThreshold',
            'LowerThreshold',
            'VMmigrations',
            'MonitoringInterval'
        )
    
MPS=(
    (1 , "MPS example 1"),
    (2 , "MPS example 2")
)



class HostForm(forms.Form):
    key = forms.IntegerField(required=True, label='Key', min_value=0)
    amount = forms.IntegerField(required=True, label='amount', min_value=0)
    ram = forms.FloatField(required=True, label='Ram', min_value=0)
    Bandwidth = forms.FloatField(required=True, label='Bandwidth', min_value=0)
    Storage = forms.FloatField(required=True, label='Storage', min_value=0)
    MaxPower = forms.IntegerField(required=True, label='MaxPower', min_value=0)
    StaticPower = forms.IntegerField(required=True, label='StaticPower', min_value=0)
    ProcessingElement = forms.IntegerField(required=True, label='Processing Element', min_value=0)
    MPS = forms.ChoiceField(required=True, label='MPS', choices=MPS)

    class Meta :
        model = Hosts
        fields=(
            'key',
            'amount',
            'ram',
            'Bandwidth',
            'Storage',
            'MaxPower',
            'StaticPower',
            'ProcessingElement',
            'MPS'
        )


class CostForm(forms.Form):
    key = forms.IntegerField(required=True, label='Key', min_value=0)
    ProcessingCost = forms.FloatField(required=True, label='Processing Cost', min_value=0)
    MemoryCost = forms.FloatField(required=True, label='Mempory Cost', min_value=0)
    StorageCost = forms.FloatField(required=True, label='Storage Cost', min_value=0)
    BandwidthCost = forms.FloatField(required=True, label='Bandwidth Cost', min_value=0)

    class Meta :
        model = Costs
        fields=(
            'key',
            'ProcessingCost',
            'MemoryCost',
            'StorageCost',
            'BandwidthCost'
        )





