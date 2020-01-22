use std::collections::HashMap;
use std::error::Error;
use std::result::Result;

use chrono::prelude::*;
use reqwest;
use serde::Deserialize;
use uuid::Uuid;

#[derive(Deserialize, Debug)]
struct Message {
    text: String,
    timestamp: DateTime<Utc>,
    sender: Uuid,
}

#[derive(Deserialize, Debug)]
struct Rating {
    interesting: u8,
    upbeat: u8,
    witty: u8,
}

#[derive(Deserialize, Debug)]
struct Conversation {
    prompt: Option<String>,
    start: DateTime<Utc>,
    ratings: Option<Rating>,
    messages: Vec<Vec<Message>>,
}

// type Dataset = HashMap<String, HashMap<String, Value>>;
type Dataset = HashMap<Uuid, Conversation>;

fn main() -> Result<(), Box<dyn Error>> {
    let data: Dataset = reqwest::get("https://git.io/ccc-dataset")?.json()?;

    for (_id, convo) in &data {
        for message in &convo.messages {
            for utterance in message {
                println!("{}", &utterance.text);
            }
        }
    }

    Ok(())
}
