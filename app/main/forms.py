from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EditArtifactForm(FlaskForm):
    objectID = StringField('Object ID', validators=[Length(0, 10), DataRequired()])
    isHighlight = StringField('Highlighted', validators=[Length(0, 50)])
    accessionNumber = StringField('Accession Number', validators=[Length(0, 50)])
    accessionYear = StringField('Accession Year', validators=[Length(0, 50)])
    isPublicDomain = StringField('Public Domain', validators=[Length(0, 50)])
    primaryImage = TextAreaField('Primary Image')
    primaryImageSmall = TextAreaField('Primary Image Small')
    department = StringField('Department', validators=[Length(0, 100)])
    objectName = StringField('Object Name', validators=[Length(0, 50)])
    title = StringField('Title', validators=[Length(0, 100)])
    culture = StringField('Culture', validators=[Length(0, 50)])
    period = StringField('Period', validators=[Length(0, 100)])
    dynasty = StringField('Dynasty', validators=[Length(0, 100)])
    reign = StringField('Reign', validators=[Length(0, 100)])
    portfolio = StringField('Portfolio', validators=[Length(0, 100)])
    artistRole = StringField('Artist Role', validators=[Length(0, 50)])
    artistPrefix = StringField('Artist Prefix', validators=[Length(0, 50)])
    artistDisplayName = StringField('Display Name', validators=[Length(0, 200)])
    artistDisplayBio = StringField('Display Bio', validators=[Length(0, 200)])
    artistSuffix = StringField('Artist Suffix', validators=[Length(0, 50)])
    artistAlphaSort = StringField('Alpha Sort', validators=[Length(0, 100)])
    artistNationality = StringField('Nationality', validators=[Length(0, 50)])
    artistBeginDate = StringField('Begin Date', validators=[Length(0, 50)])
    artistEndDate = StringField('End Date', validators=[Length(0, 50)])
    artistGender = StringField('Artist Gender', validators=[Length(0, 50)])
    artistWikiDataURL = StringField('Artist Wiki Data URL', validators=[Length(0, 200)])
    artistULAN_URL = StringField('Artist ULAN URL', validators=[Length(0, 200)])
    objectDate = StringField('Object Date', validators=[Length(0, 100)])
    objectBeginDate = StringField('Object Begin Date', validators=[Length(0, 50)])
    objectEndDate = StringField('Object End Date', validators=[Length(0, 50)])
    medium = StringField('Medium', validators=[Length(0, 50)])
    dimensions = StringField('Dimensions', validators=[Length(0, 50)])
    measurements = TextAreaField('Measurements')
    creditLine = StringField('Credit Line', validators=[Length(0, 100)])
    geographyType = StringField('Geography Type', validators=[Length(0, 100)])
    city = StringField('City', validators=[Length(0, 50)])
    state = StringField('State', validators=[Length(0, 50)])
    county = StringField('County', validators=[Length(0, 50)])
    country = StringField('Country', validators=[Length(0, 50)])
    region = StringField('Region', validators=[Length(0, 50)])
    subregion = StringField('Sub Region', validators=[Length(0, 50)])
    locale = StringField('Locale', validators=[Length(0, 50)])
    locus = StringField('Locus', validators=[Length(0, 50)])
    excavation = StringField('Excavation', validators=[Length(0, 100)])
    river = StringField('River', validators=[Length(0, 50)])
    classification = StringField('Classification', validators=[Length(0, 50)])
    rightsAndReproduction = StringField('Rights and Reproduction', validators=[Length(0, 50)])
    linkResource = StringField('Link Resource', validators=[Length(0, 200)])
    metadataDate = StringField('Metadata Date', validators=[Length(0, 50)])
    repository = StringField('Repository', validators=[Length(0, 100)])
    objectURL = StringField('Object URL', validators=[Length(0, 100)])
    tags = TextAreaField('Tags')
    objectDataWikiURL = StringField('ObjectData Wiki URL', validators=[Length(0, 200)])
    isTimeLineWork = StringField('Timeline Work', validators=[Length(0, 50)])
    galleryNumber = StringField('Gallery Number', validators=[Length(0, 50)])
    constituentID = StringField('Constituent ID', validators=[Length(0, 50)])
    role = StringField('Role', validators=[Length(0, 50)])
    name = StringField('Name', validators=[Length(0, 100)])
    constituentULANURL = StringField('Constituent ULAN URL', validators=[Length(0, 200)])
    constituentWikiDataURL = StringField('Constituent WikiData URL', validators=[Length(0, 200)])
    gender = StringField('Gender', validators=[Length(0, 50)])
    submit = SubmitField('Submit')

    def __init__(self, artifact, *args, **kwargs):
        super(EditArtifactForm, self).__init__(*args, **kwargs)
        self.artifact = artifact
