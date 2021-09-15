xpath_template = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]"
xpath_unique_answer = "//*[@id=\"mainContent\"]/div[2]/div[<NUM>]/div/div/div/div/div/div/div"

window.getElementByXPath = (path)=> { 
    return (new XPathEvaluator()) 
        .evaluate(path, document.documentElement, null, 
                        XPathResult.FIRST_ORDERED_NODE_TYPE, null) 
        .singleNodeValue; 
} 

window.is_answer = (idx) => {
    xp = xpath_unique_answer.replace("<NUM>",idx.toString())
    return getElementByXPath(xp) != null
}
