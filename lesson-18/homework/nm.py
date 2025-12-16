import pandas as pd
questions = pd.read_csv('tackoverflow_qa.csv')
questions.head()

cre_date = questions.creationdate
questions[cre_date < '2014-01-01']

scores = questions.score
questions[scores > 50]
questions[scores.between(50, 100)]

questions[questions["ans_name"] == "Scott Boston"]

users = ['User1', 'User2', 'User3', 'User4', 'User5']

questions[questions['ans_name'].isin(users)]

questions[
    (questions['creationdate'].between('2014-03-01', '2014-10-31')) &
    (questions['ans_name'] == 'Unutbu') &
    (questions['score'] < 5)
]

questions[
    (questions['score'].between(5, 10)) |
    (questions['viewcount'] > 10000)
]

questions[questions["ans_name"] != "Scott Boston"]



import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic.head()

titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Age'].between(20, 30))
]

titanic[titanic['Fare'] > 100]

titanic[
    (titanic['Survived'] == 1) &
    (titanic['SibSp'] == 0) &
    (titanic['Parch'] == 0)
]

titanic[
    (titanic['Embarked'] == 'C') &
    (titanic['Fare'] > 50)
]

titanic[
    (titanic['SibSp'] > 0) &
    (titanic['Parch'] > 0)
]

titanic[(titanic['Age'] <= 15) &
    (titanic['Survived'] == 0)
]
          
titanic[titanic['PassengerId'] % 2 == 1]

titanic['Ticket'].value_counts()

titanic[
    (titanic['Name'].str.contains('Miss', na=False)) &
    (titanic['Pclass'] == 1)
]


