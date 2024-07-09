import pandas as pd

from pgmpy.base import DAG
from pgmpy.estimators import PC, HillClimbSearch, ExpertInLoop
from pgmpy.metrics import implied_cis, fisher_c
from pgmpy.estimators.CITests import ci_pillai


def preprocess_data():
    df = pd.read_csv("adult_proc.csv", index_col=0)
    df.Age = pd.Categorical(
        df.Age,
        categories=["<21", "21-30", "31-40", "41-50", "51-60", "61-70", ">70"],
        ordered=True,
    )
    df.Education = pd.Categorical(
        df.Education,
        categories=[
            "Preschool",
            "1st-4th",
            "5th-6th",
            "7th-8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "HS-grad",
            "Some-college",
            "Assoc-voc",
            "Assoc-acdm",
            "Bachelors",
            "Prof-school",
            "Masters",
            "Doctorate",
        ],
        ordered=True,
    )
    df.HoursPerWeek = pd.Categorical(
        df.HoursPerWeek, categories=["<=20", "21-30", "31-40", ">40"], ordered=True
    )
    df.Workclass = pd.Categorical(df.Workclass, ordered=False)
    df.MaritalStatus = pd.Categorical(df.MaritalStatus, ordered=False)
    df.Occupation = pd.Categorical(df.Occupation, ordered=False)
    df.Relationship = pd.Categorical(df.Relationship, ordered=False)
    df.Race = pd.Categorical(df.Race, ordered=False)
    df.Sex = pd.Categorical(df.Sex, ordered=False)
    df.NativeCountry = pd.Categorical(df.NativeCountry, ordered=False)
    df.Income = pd.Categorical(df.Income, ordered=False)
    return df


df = preprocess_data()

est = PC(df.copy())
dag_chisq = est.estimate(ci_test="chi_square", return_type="cpdag")
dag_chisq.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_x2.png", prog="dot"
)

est = PC(df.copy())
dag_pillai = est.estimate(ci_test="pillai", return_type="cpdag")
dag_pillai.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_pillai.png", prog="dot"
)

est = HillClimbSearch(df.copy())
dag_bic = est.estimate(scoring_method="bicscore")
dag_bic.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_bic.png", prog="dot"
)

est = HillClimbSearch(df.copy())
dag_bic_blacklist = est.estimate(scoring_method="bicscore", black_list=[('Sex', 'MaritalStatus'), ('MaritalStatus', 'Income'), ('Income', 'Education'), ('MaritalStatus', 'Age'), ('Income', 'HoursPerWeek')])
dag_bic_blacklist.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_bic_blacklist.png", prog="dot"
)

est = HillClimbSearch(df.copy())
start_dag=DAG([('Age', 'Income'),
               ('Age', 'Education'),
               ('Age', 'MaritalStatus'),
               ('Age', 'HoursPerWeek'),
               ('NativeCountry', 'Race'),
               ('HoursPerWeek', 'Income'),
               ('Education', 'Occupation'),
               ('Education', 'Income'),
               ('Education', 'Workclass'),
               ('Occupation', 'Income'),
               ('Sex', 'Income'),
               ('Relationship', 'MaritalStatus'),
               ])
dag_bic_start = est.estimate(scoring_method="bicscore", start_dag=start_dag)
dag_bic_start.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_bic_start.png", prog="dot"
)

est = HillClimbSearch(df.copy())
dag_bic_fixed = est.estimate(scoring_method="bicscore", fixed_edges=[('HoursPerWeek', 'Income'), ('Education', 'Income'), ('Sex', 'Income'), ('Occupation', 'Income'), ('Workclass', 'Income')])
dag_bic_fixed.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_bic_fixed.png", prog="dot"
)

descriptions = {
    "Age": "The age of a person",
    "Workclass": "The workplace where the person is employed such as Private industry, or self employed",
    "Education": "The highest level of education the person has finished",
    "MaritalStatus": "The marital status of the person",
    "Occupation": "The kind of job the person does. For example, sales, craft repair, clerical",
    "Relationship": "The relationship status of the person",
    "Race": "The ethnicity of the person",
    "Sex": "The sex or gender of the person",
    "HoursPerWeek": "The number of hours per week the person works",
    "NativeCountry": "The native country of the person",
    "Income": "The income i.e. amount of money the person makes",
}
dag_llm = ExpertInLoop(df.copy()).estimate(variable_descriptions=descriptions)
dag_llm.to_graphviz().draw(
    "../work/presentations/2024_07_scipy/imgs/adult_llm.png", prog="dot"
)

imp_cis = implied_cis(dag_llm, df.copy(), ci_test=ci_pillai)

fisherc_pval = fisher_c(dag_bic_fixed, df.copy(), ci_test=ci_pillai)
fisherc_pval = fisher_c(dag_llm, df.copy(), ci_test=ci_pillai)

structure_score(dag_bic_fixed, df, scoring_method='bic')
structure_score(dag_llm, df, scoring_method='bic')
