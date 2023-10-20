"""   
(5) Implement a function called list_tagger. The list_tagger function will accept a single
parameter, a list called batch. This function must determine the length of the list, insert the length as an
int into the list at the beginning of the list, and return the new list. That is, we will tag the list passed to the
function with its length, and return it. You may assume for this question that you do not need to perform
any parameter checking. That is, you may assume that the parameter is a list. Include a docstring. Inside
the docstring, include a doctest for an empty list and a doctest for a non-empty list.
"""


def list_tagger(batch: list):
    """
    Insert the length of batch at the beginning of batch.

    :param batch: a list
    :precondition: batch can be empty
    :postconditin: insert the length of batch at the beginning of batch
    :return: a list
    >>> list_tagger([0,1,2,3,4,5])
    [6, 0, 1, 2, 3, 4, 5]
    >>> list_tagger([])
    [0]
    """

    batch.insert(0,len(batch))
    return batch

def main():
    print(list_tagger([0,1,2,3,4,5]))
    print(list_tagger([]))


if __name__ == "__main__":
    main()
