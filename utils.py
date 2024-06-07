import pandas as pd
import numpy as np

joe_proclamation = pd.read_csv("documents_signed_by_joseph_r_biden_jr_of_type_presidential_document_and_of_presidential_document_type_proclamation.csv")
joe_executive = pd.read_csv("documents_signed_by_joseph_r_biden_jr_of_type_presidential_document_and_of_presidential_document_type_executive_order.csv")
donald_proclamation = pd.read_csv("documents_signed_by_donald_trump_of_type_presidential_document_and_of_presidential_document_type_proclamation.csv")
donald_executive = pd.read_csv("documents_signed_by_donald_trump_of_type_presidential_document_and_of_presidential_document_type_executive_order.csv")



def get_executive_order():
    if len(donald_executive) > 0 and len(joe_executive) > 0:
        if np.random.randint(2) == 0:
          
            return "Donald", donald_executive.sample(1)
        else:
            return "Joe", joe_executive.sample(1)



