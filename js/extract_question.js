window.get_all_answer_div = () => {
    var ans = []
    list_ele = document.getElementsByClassName("CssComponent-sc-1oskqb9-0 cXjXFI")
    for(var i = 0 ; i < list_ele.length ; i++) {
        if(window.is_answer(i)) {
        ans.push([list_ele[i],i])
    }
    }
    return ans
}


