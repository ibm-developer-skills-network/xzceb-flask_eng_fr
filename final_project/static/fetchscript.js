async function to_english() {
    try {
        const response = await fetch("127.0.0.1:500/frenchToEnglish");
        if (!response.ok) {
            throw new Error(`Error in fetching translated word: ${response.status}`)
        }
        print_to_div(response.json())
    }
    catch(e){
        print_to_div(e)
    }
}

function print_to_div(text){
    document.getElementById("translated_text").textContent = text
}

async function to_french() {
    try {
        const response = await fetch("127.0.0.1:500/englishToFrench");
        if (!response.ok) {
            throw new Error(`Error in fetching translated word: ${response.status}`)
        }
        print_to_div(response.json())    }
    catch(e) {
print_to_div(e)    }
}
