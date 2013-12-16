from django.db import models

class PaperManager(models.Manager):
    '''
    This class is the Manager of Paper class.
    '''
    
    def paper_exists(self, mendeley_id):
        '''
        This function checks if a paper exists.
        @param mendeley_id: The paper's Mendeley id.  
        '''
        return self.filter(mendeley_id = mendeley_id).exists() 
    
    def get_papers_to_complete(self):
        '''
        Return papers which its information is incomplete.
        '''
        return self.filter(abstract='').exclude(abstract='No abstract.')
    
    def count_papers(self, category = None):
        '''
        This function returns the quantity of papers given a category.
        @param category: A instance of Category class. The parameter accepts empty.
        '''
        if category == None:
            return self.all().count()
        else:
            return self.filter(category = category).count()
         
    
class Paper(models.Model):
    '''
    This class represents a Paper.
    @ivar title: A string containing the title of the paper.
    @ivar mendeley_id: The paper's id in Mendeley website.
    @ivar year: The year which the paper was published.
    @ivar abstract: The abstract of the paper.
    @ivar publiction_outlet: The name of the publisher. 
    @ivar doi: The paper's doi.
    @ivar categories: The category of the paper according to the Mendeley's classification.
    @ivar identifiers: The Doi, ISSN, PMID of the paper.
    @ivar issue: The issue which the paper was published.
    @ivar pages: The quantity of papers of the paper.
    @ivar stats: 
    @ivar mendeley_url: The link of the paper in Mendeley.
    @ivar paper_type: 
    @ivar volume: Volume which the paper was published.
    @ivar public_file_hash: 
    @ivar paper_topic: 
    @ivar keywords: 
    
    '''
    title               = models.CharField(max_length = 500)
    #using null because of the papers that are not in mendeley
    mendeley_id         = models.CharField(max_length = 255, null = True, unique = True)
    year                = models.PositiveIntegerField(null=True)
    abstract            = models.TextField(blank=True)
    publication_outlet  = models.CharField(max_length = 300, blank = True)
    doi                 = models.CharField(max_length = 300, blank = True)
    mendeley_url        = models.URLField(blank=True, max_length=300)
    
    categories          = models.TextField(max_length = 300, blank = True)
    identifiers         = models.CharField(max_length = 300, blank = True)
    issue               = models.CharField(max_length = 300, blank = True)
    pages               = models.CharField(max_length = 300, blank = True)
    stats               = models.TextField(max_length = 300, blank = True)
    paper_type          = models.CharField(max_length = 300, blank = True)
    volume              = models.CharField(max_length = 300, blank = True)
    public_file_hash    = models.CharField(max_length = 300, blank = True)   
    paper_topic         = models.CharField(max_length = 500, blank = True)
    keywords            = models.CharField(max_length = 500, blank = True)
    
    objects = PaperManager()
    
    def get_description(self):
        '''
        Get the paper's title and abstract.
        '''
        return self.title + self.abstract
    
    def __unicode__(self):
        return str(self.title) 
################################################################################
