library(tesseract)

pngfile <- pdftools::pdf_convert("mozilla.pdf", dpi = 600)
text <- tesseract::ocr(pngfile)

library(magick)
image_read("mozilla_page7.png") |> image_convert(type = 'White') |> image_write("mozilla_page7_test.png")

#tesseract -l eng+ara  mozilla_page3.png klm_ar
