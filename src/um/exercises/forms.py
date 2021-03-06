"""Form definitions."""
from braces.forms import UserKwargModelFormMixin

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Field, Fieldset, Submit

from django import forms
from django.utils.translation import gettext_lazy as _

from um.core.constants import LICENCE_CHOICES_LONG
from .models import Exercise


class ExerciseForm(UserKwargModelFormMixin, forms.ModelForm):
    """ModelForm for the Exercise model."""

    class Meta:  # noqa: D101
        model = Exercise
        fields = [
            'text',
            'license',
            'author',
            'is_original',
            'original_author',
            'source_url',
            'changes',
        ]

        labels = {
            'text': None,
        }
        help_texts = {
            'text': 'Markdown und LaTeX mit $ und $$.',
        }

    def __init__(self, *args, **kwargs):
        """Add crispy-forms helper and layout to form."""
        super(ExerciseForm, self).__init__(*args, **kwargs)

        # add Crispy Forms foo
        self.helper = FormHelper()
        self.helper.form_id = 'id-ExerciseForm'
        self.helper.add_input(Submit('continue', 'Save & continue editing'))
        self.helper.add_input(Submit('save', 'Save'))

        self.helper.layout = Layout(
            Fieldset(
                _('exercise text'),
                Field(
                    'text',
                    v_model='input',
                    css_class='editor-input',
                ),
                'license',
                'author',
                Field(
                    'is_original',
                    v_model='is_original',
                ),
                Div(
                    'original_author',
                    'source_url',
                    'changes',
                    v_if='is_original == false'
                ),
            ),
        )
        self.fields['text'].label = False
        self.fields['author'].required = False
        self.fields['license'].choices = LICENCE_CHOICES_LONG
        self.fields['is_original'].default = True
        self.fields['original_author'].required = False
        self.fields['source_url'].required = False
        self.fields['changes'].required = False

        if self.user and not self.user.is_staff:
            # don't let normal users change the author field
            self.fields['author'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(ExerciseForm, self).clean()
        original_author = cleaned_data.get('original_author')
        source_url = cleaned_data.get('source_url')
        changes = cleaned_data.get('changes')

        if original_author and source_url == '':
            # If source is given, then a source URL is required.
            raise forms.ValidationError(
                _('Please provide a URL for the source.')
            )

        if original_author and changes == '':
            # If source is given, then info about changes to the exercise is required.
            raise forms.ValidationError(
                _('Please describe the changes made to the exercise.')
            )

    def clean_original_author(self):
        """If exercise is an original, wipe all source information."""
        original_author = self.cleaned_data['original_author']
        is_original = self.cleaned_data['is_original']

        if is_original:
            return None

        return original_author

    def clean_source_url(self):
        """If exercise is an original, wipe all source information."""
        source_url = self.cleaned_data['source_url']
        is_original = self.cleaned_data['is_original']

        if is_original:
            return ''

        return source_url
