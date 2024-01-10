use rust_bert::pipelines::question_answering::{QaInput, QuestionAnsweringModel};

fn main() {
    let qa_model = QuestionAnsweringModel::new(Default::default()).unwrap();

    let question = String::from(
        "I run an online shoe store. Give me recommendations for how to reduce emissions.",
    );
    let context = String::from(
        r#"
Your goal is to provide valuable suggestions to a company for reducing their climate change emissions. You will receive examples of actions submitted by companies with similar emissions reduction goals.

Given the current company's "Scope and Category" and "Source" of emissions, please provide one or more actionable suggestions that align with the company's goals and constraints. Consider the following when providing suggestions:

- The company's specific emissions reduction targets or objectives
- Any customization requests or constraints mentioned by the company
- The feasibility and practicality of the suggested actions
- The potential impact of the actions on reducing emissions

Your suggestions should be concise and clear, either as a few sentences or a brief list. Focus on providing suggestions that are aligned with the company's goals and constraints. 

If you need any clarification or additional information, feel free to ask.
    "#,
    );

    let answers = qa_model.predict(&[QaInput { question, context }], 1, 32);
}
