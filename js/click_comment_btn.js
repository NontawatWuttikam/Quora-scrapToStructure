for(i = 0 ; i < buto.length ; i++){
    if (buto[i].ariaLabel != null)
    if (buto[i].ariaLabel.includes("comment")) {
    buto[i].click()
}
}