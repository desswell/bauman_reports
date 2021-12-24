
from behave import given, when, then
from main import get_roots


@given(u"Biquadratic equation app is run")
def step_impl(context):
    print(u'Step: Given Biquadratic equation app is run')

@when(u'I have the odds "{a}", "{b}", and "{c}"')
def step_impl(context, a, b, c):
    print(f'Step: I have the odds "{a}", "{b}", and "{c}"')
    b = str(get_roots(int(a), int(b), int(c))).rpartition(']')[0]
    c = b.partition('[')[2]
    context.result = c
    print(f'Stored result "{context.result}" in context')

@then(u'I get result "{out}"')
def step_impl(context, out):
    if (context.result == str(out)):
        print(f'Step: Then I get right result "{context.result}", "{out}"')
        pass
    else :
        raise Exception ("Invalid root is returned.")