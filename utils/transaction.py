class Transaction:
    def __init__(self, trans_id, state, date, operationAmount_amount,
                 operationAmount_currency_name, operationAmount_currency_code, description, from_field, to):
        self.id = trans_id
        self.state = state
        self.date = date
        self.operationAmount_amount = operationAmount_amount
        self.operationAmount_currency_name = operationAmount_currency_name
        self.operationAmount_currency_code = operationAmount_currency_code
        self.description = description
        self.from_field = from_field
        self.to = to


    def __repr__(self):
        return f'User(id={self.id}, ' \
               f'state={self.state}, ' \
               f'date={self.date}, ' \
               f'operationAmount_amount={self.operationAmount_amount}, ' \
               f'operationAmount_currency_name={self.operationAmount_currency_name}, ' \
               f'operationAmount_currency_code={self.operationAmount_currency_code}, ' \
               f'description={self.description}, ' \
               f'from_field={self.from_field},' \
               f' to={self.to})'

