const fs = require('fs');
const pdf = require('pdf-parse');

async function extractText(pdfPath) {
    try {
        let dataBuffer = fs.readFileSync(pdfPath);
        let data = await pdf(dataBuffer);
        console.log(`\n\n--- CONTENT FROM: ${pdfPath} ---\n\n`);
        console.log(data.text);
    } catch (e) {
        console.error(`Error reading ${pdfPath}:`, e);
    }
}

async function main() {
    await extractText('./Store_Design_Standards_Official.pdf');
    await extractText('./2_Days_Intensive_Shopify_Training_Official.pdf');
}

main();
