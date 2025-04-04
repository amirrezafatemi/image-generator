import os
import flet
import replicate
import requests

"""
Hi therw (:
I am Amirreza Fatemi. (there is also a suffix in my name which is "Salanghoch")
This python script allow you to generate any image by using flux.dev from blackforestlabs (https://blackforestlabs.ai/).
To run this script you may need an API token you can get it by setting up an account in https://replicate.com/black-forest-labs/flux-dev/api.
Then after that, you also should set up billing to run this model. Go to https://replicate.com/account/billing#billing to set it up. Better to check https://replicate.com/account/api-tokens too.
"""

# your API token should be something like "r8_**********lgN6seRptoxwr5rgurnwU3l35ny"
os.environ["REPLICATE_API_TOKEN"] = "YOUR_API_TOKEN"

def generate_image(prompt):
    try:
        _output=replicate.run(
            "black-forest-labs/flux-dev",
            # getting "black-forest-labs/flux-dev" via Replicate
            # if you are wandering why these parameters check out https://replicate.com/bingbangboom-lab/flux-dreamscape?input=python
            input={
                "prompt": prompt,
                "go_fast": True,
                "guidance": 3.5,
                "megapixels": "1",
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "webp",
                "output_quality": 80,
                "prompt_strength": 0.8,
                "num_inference_steps": 28
            }
        )
        return _output[0]
    except Exception as error:
        print(f"Error: {error}") 
        return None   

def save_image(image_url, filename="generated_image.webp"):
    try:
        _response=requests.get(image_url)
        if _response.status_code == 200:
            with open(filename,"wb") as f:
                f.write(_response.content)
            print(f"Image Saved Successfully As {filename}")
        else:
            print(f"Failed To Download The Image.\nStatus code: {_response.status_code}")
        #Github: amirrezafatemi/image-generator
    except Exception as error:
        print(f"""Error Saving Image
                ERROR(s) Indicates:
                {error}""")

def main(page: flet.Page):
    page.title="Image Generator (By AmirRezaFatemi)"
    page.horizontal_alignment="center"
    page.scroll=flet.ScrollMode.AUTO

    page.appbar=flet.AppBar(
        title=flet.Text(value="Image Generator",color="Black"),
        center_title=True,
        bgcolor="greyAccent200"
    )

    _result_image=flet.Image(
        src="https://via.placeholder.com/512",width=512,height=512
    )

    _save_image_button=flet.ElevatedButton(
        text="Save Image",disabled=True,
        style=flet.ButtonStyle(
            color={
                flet.ControlState.HOVERED: flet.colors.BLACK,
                flet.ControlState.FOCUSED: flet.colors.BLACK,
                flet.ControlState.DEFAULT: flet.colors.WHITE,
            },
            bgcolor={flet.ControlState.FOCUSED: flet.colors.BLACK, "": flet.colors.WHITE,
                     flet.ControlState.HOVERED: flet.colors.WHITE, "": flet.colors.BLACK},
            padding={flet.ControlState.HOVERED: 20},
            overlay_color=flet.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=1000,
            side={
                flet.ControlState.DEFAULT: flet.BorderSide(2,flet.colors.BLACK),
                flet.ControlState.HOVERED: flet.BorderSide(1,flet.colors.BLACK),
            },
            shape={
                flet.ControlState.HOVERED: flet.RoundedRectangleBorder(radius=20),
                flet.ControlState.DEFAULT: flet.RoundedRectangleBorder(radius=3)
            },
        )
    )

    def generate_and_display_image(e):
        _prompt=_prompt_input.value
        if _prompt:
            page.splash=flet.ProgressBar()
            page.update()

            _image_url=generate_image(_prompt)
            page.splash=None

            if _image_url:
                _result_image.src=_image_url
                _result_image.update()
                _save_image_button.disabled=False
                _save_image_button.update()
                def save_image_click(e):
                    save_image(_image_url,"image.webp")
                _save_image_button.on_click=save_image_click

            else:
                page.dialog=flet.AlertDialog(
                    title=flet.Text("An Error Has Occured"),
                    content=flet.Text("Failed To Generate Image. Please Try Again."),
                    actions=[
                        flet.TextButton(
                            "OK",on_click=lambda _: page.dialog.close()
                        )
                    ]
                )
                page.dialog.open=True
                page.update()


    _prompt_input=flet.TextField(
        label="Enter A Text Prompt",
        hint_text="Decribe Your Picture",
        border_color="Black",
        focused_color="Black"
        )

    _generate_button=flet.ElevatedButton(
        text="Generate Image",on_click=generate_and_display_image,
        style=flet.ButtonStyle(
            color={
                flet.ControlState.HOVERED: flet.colors.BLACK,
                flet.ControlState.FOCUSED: flet.colors.BLACK,
                flet.ControlState.DEFAULT: flet.colors.WHITE,
            },
            bgcolor={flet.ControlState.FOCUSED: flet.colors.BLACK, "": flet.colors.WHITE,
                     flet.ControlState.HOVERED: flet.colors.WHITE, "": flet.colors.BLACK},
            padding={flet.ControlState.HOVERED: 20},
            overlay_color=flet.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=1000,
            side={
                flet.ControlState.DEFAULT: flet.BorderSide(2,flet.colors.BLACK),
                flet.ControlState.HOVERED: flet.BorderSide(1,flet.colors.BLACK),
            },
            shape={
                flet.ControlState.HOVERED: flet.RoundedRectangleBorder(radius=20),
                flet.ControlState.DEFAULT: flet.RoundedRectangleBorder(radius=3)
            },
        )
    )

    page.add(
        flet.SafeArea(
            content=flet.Column(
                [
                    _prompt_input, _generate_button,
                    _result_image,_save_image_button
                ],
                horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
        ),
    )

flet.app(main)
