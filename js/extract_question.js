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

window.get_all_answer_div = () => {
    var ans = []
    list_ele = getElementByXPath("//*[@id=\"mainContent\"]/div[2]").children
    for(var i = 0 ; i < list_ele.length ; i++) {
        if(is_answer(i)) {
        ans.push(list_ele[i])
    }
    }
    return ans
}


