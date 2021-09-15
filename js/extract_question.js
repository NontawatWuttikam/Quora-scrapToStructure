window.get_all_answer_div = () => {
    var ans = []
    list_ele = window.getElementByXPath("//*[@id=\"mainContent\"]/div[2]").children
    for(var i = 0 ; i < list_ele.length ; i++) {
        if(window.is_answer(i)) {
        ans.push(list_ele[i])
    }
    }
    return ans
}


