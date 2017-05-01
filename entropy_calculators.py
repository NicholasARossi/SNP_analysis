from collections import Counter
import math
class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of values from the
        two distributions.

        other: Pmf

        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf



def H(input_list):
    rez=Pmf(input_list)
    rez.normalize()
    entropy=0
    for key, prob in rez.items():
        entropy += - prob*math.log(prob, 2)
    return entropy

if __name__ == '__main__':


    #### Unit Tests ####
    import pandas as pd

    file = 'human_test_data.csv'
    tp = pd.read_csv(file, iterator=True, chunksize=100)
    df = pd.concat(tp, ignore_index=True)

    ### remove unwanted columns
    del df['rs_number']
    del df['Unnamed: 0']

    Total_entropy = 0
    for index, row in df.iterrows():
        temp_list=row.tolist()
        Total_entropy += H(temp_list)

    average_entropy=Total_entropy/df.shape[0]
    print("Average entropy of Human test = " +str(average_entropy)+'\n')

    ### Wheat Unit Test
    file = 'wheat_test_data.csv'
    df2 = pd.read_csv(file, nrows=5)

    #remove unwanted column
    del df2['Unnamed: 0']
    Total_entropy = 0
    for index, row in df2.iterrows():
        temp_list=row.tolist()

        #remove unsequenced wheat strain data
        list(filter(('NS').__ne__, temp_list))
        Total_entropy += H(temp_list)
    average_entropy = Total_entropy / df2.shape[0]
    print("Average entropy of Wheat test = "+ str(average_entropy)+"\n")
