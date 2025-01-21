import replicate
import os


os.environ['REPLICATE_API_TOKEN']='sk-none'
input = {
    "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot"
}

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input=input
)
print(output)
#=> ["https://replicate.delivery/yhqm/hcDDSNf633zeDUz9sWkKfaf...