from django.shortcuts import render
from math import sqrt

def quadratic_results(request):
    context = {}
    key_error = ''
    message = ''
    for key, value in request.GET.items():
        if key == 'a' and value == '0':
            key_error = '{}_error'.format(key)
            message = 'coefficient at the first term of the equation cannot be equal to zero'
        elif not value:
            key_error = '{}_error'.format(key)
            message = 'coefficient undefined'
        else:
            try:
                value = int(value)
            except:
                if ValueError:
                    key_error = '{}_error'.format(key)
                    message = 'coefficient is not an integer'
        context[key] = value
        context[key_error] = message

    results = {}
    if type(context['a']) == int and type(context['b']) == int and type(context['c']) == int:
        discriminat = context['b'] ** 2 - 4 * context['a'] * context['c']
        results['discriminant'] = discriminat
        if discriminat >= 0:
            x1 = (- context['b'] + sqrt(discriminat)) / (2 * context['a'])
            x2 = (- context['b'] - sqrt(discriminat)) / (2 * context['a'])
            results['x1'] = x1
            results['x2'] = x2

    return render(request, 'results.html', {'context': context, 'results': results})
