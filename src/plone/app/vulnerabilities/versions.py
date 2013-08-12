from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

DUMMY_VERSION_LIST = ['4.3.1', '4.3', '4.2.5', '4.2.4', '4.2.3', '4.2.2', '4.2.1', '4.2', '4.1.6', '4.1.5', '4.1.4', '4.1.3', '4.1.2', '4.1.1', '4.1', '4.0.9', '4.0.7', '4.0.5', '4.0.4', '4.0.3', '4.0.2', '4.0.1', '4.0', '3.3.6', '3.3.5', '3.3.4', '3.3.3', '3.3.2', '3.3.1', '3.3', '3.2.3', '3.2.2', '3.2.1', '3.2', '3.1.7', '3.1.6', '3.1.5.1', '3.1.4', '3.1.3', '3.1.2', '3.1.1', '3.1', '3.0.6', '3.0.5', '3.0.4', '3.0.3', '3.0.2', '3.0.1', '3.0', '2.5.5', '2.5.4', '2.5.3', '2.5.2', '2.5.1', '2.5', '2.1.4', '2.1.3', '2.1.2', '2.1.1', '2.1', '2.0.5', '2.0.4', '2.0.3', '2.0.2', '2.0.1', '2.0', '1.0.6', '1.0.5', '1.0.4', '1.0.3', '1.0.2', '1.0.1', '1.0']


def plone_version_vocabulary(context):
    terms = []
    
    for version in DUMMY_VERSION_LIST:
        # value,token,title
        terms.append(SimpleTerm(version,version,version))
    
    # XXX: Should probably include series (4.x, 4.2.x, 3.3.x etc)
    
    result = SimpleVocabulary(terms)
    return result
        
        