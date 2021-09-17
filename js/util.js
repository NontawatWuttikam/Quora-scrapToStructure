xpath_template = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]"
xpath_unique_answer = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]/div/div/div/div/div/div/div"

window.getElementByXPath = (path)=> { 
    return (new XPathEvaluator()) 
        .evaluate(path, document.documentElement, null, 
                        XPathResult.FIRST_ORDERED_NODE_TYPE, null) 
        .singleNodeValue; 
} 

window.is_answer = (idx) => {
    txt = window.getElementByXPath("//*[@id=\"mainContent\"]/div[2]").children[idx].textContent
    if(txt == null) return false
    return !txt.includes("Ad by") & !txt.includes("Sponsored") & !txt.includes("AnswersAsked") & !txt.includes("Related Questions") & !txt.includes("Promoted by")
}
