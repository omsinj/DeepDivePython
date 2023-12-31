from random import choice

def random_exception(*exceptions):
    raise choice(exceptions)

try:
    random_exception(
        OSError('os broke?'), 
        IndexError('not cool'), 
        AttributeError('where did it go?'), 
        KeyboardInterrupt,
        SystemError,
    )
    # Specific exceptions can be handled independently.
except OSError as ex:
    print('os errors are the worst')
    print(ex)
    # Multiple exceptions can be handled within the same except block.
except (IndexError, AttributeError) as ex:
    print('wrong index or missing attribute, we have a problem.')
    print(ex)
    # Exception handlers don't have to name-bind the exception.
except KeyboardInterrupt:
    print('stop interrupting me')
    # Omitting an exception handles all unhandled exceptions.
except:
    print('catch all without binding exception')

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from None
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from None
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from None
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from None





