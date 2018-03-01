python3 label_image/label_image.py \
--graph=quantized_graph.pb --labels=output_labels.txt \
--input_layer=input \
--output_layer=final_result \
--input_height=224 --input_width=224 \
--input_mean=128 --input_std=128 \
--image=images.jpg
