library(webshot)
html_files <- list.files(pattern = ".html$", recursive = TRUE)
for(i in html_files){
  webshot(i, sprintf("%s", paste(i, "png", sep=".")),delay = 0.5)
  #print(sprintf("%s", paste(i, "png", sep=".")))
  print("done")
}
