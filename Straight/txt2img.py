import time



from diffusers import StableDiffusionXLPipeline
import torch

#.cache/huggingface/hub/models--stabilityai--stable-diffusion-xl-base-1.0
# pipe = StableDiffusionXLPipeline.from_pretrained(
#     "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True, add_watermarker=False
# )

pipe = StableDiffusionXLPipeline.from_pretrained(
    "/cta/users/mselvi/.cache/huggingface/hub/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/3941f478e00f9e9aa4ff75d2cb207da19663fe4a",
    torch_dtype=torch.float16, variant="fp16", use_safetensors=True, add_watermarker=False, local_files_only=True
)
pipe.to("cuda")

# prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
# prompt = "Female anime character wearing soldier uniform in a jungle, cold color palette, muted colors, detailed, 8k"
# prompt = "Three people facing to the camera while showing the camera their tablets where online certificates are seen on the screen in an office of a tech company, realistic, real portrait, canon, f/1.8, detailed, 8k, 35mm lens, f/1.8, natural lighting, global illumination"
prompt = "A minimalist logo with 3 ginkgo leaves, white background, hot color palette, minimalist, minimalism, illustration, (logo:1.5), vector image, 8k"
image = pipe(prompt=prompt).images[0]

image.save("image_"+str(time.time())+".png")

