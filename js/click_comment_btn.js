
window.click_comment_btn = () => {
    buto = document.getElementsByClassName("q-click-wrapper ClickWrapper___StyledClickWrapperBox-zoqi4f-0 bIwtPb base___StyledClickWrapper-lx6eke-1 laIUvT   qu-active--bg--darken qu-active--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--bg--darken qu-hover--textDecoration--none")
    for(i = 0 ; i < buto.length ; i++){
    if (buto[i].ariaLabel != null)
    if (buto[i].ariaLabel.includes("comment")) {
    buto[i].click()
}
}
}