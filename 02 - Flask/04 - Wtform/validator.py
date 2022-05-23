from wtforms.validators import ValidationError

# Custom validator to be used in any below class (must have sub function)
def length(min=-1, max=-1, message=""):
    message = message % (min, max)
    def _length(self, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length