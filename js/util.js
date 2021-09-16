xpath_template = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]"
xpath_unique_answer = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]/div/div/div/div/div/div/div"

window.getElementByXPath = (path)=> { 
    return (new XPathEvaluator()) 
        .evaluate(path, document.documentElement, null, 
                        XPathResult.FIRST_ORDERED_NODE_TYPE, null) 
        .singleNodeValue; 
} 

window.is_answer = (idx) => {
    txt = document.getElementsByClassName("CssComponent-sc-1oskqb9-0 cXjXFI")[idx].textContent
    if(txt == null) return false
    return !txt.includes("Ad") & !txt.includes("Sponsored")
}
