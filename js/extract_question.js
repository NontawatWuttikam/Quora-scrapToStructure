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


