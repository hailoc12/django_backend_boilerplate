import axios from 'src/utils/axios';

export const renderImage = async (rawPrompt, templateId, width=512, height=512, numOutputs=1, transactionId=null, initImage=null, guidanceScale=7.5) => {
    const response = await axios.post('/v1/render_image/', {
        raw_prompt: rawPrompt,
        render_template_id: templateId,
        width, height,
        num_outputs: numOutputs,
        transaction_id: transactionId,
        init_image: initImage,
        guidance_scale: guidanceScale,
    })

    return response.data;
}

export const getRenderTemplates = async () => {
    const response = await axios.get('/v1/render_template/');
    return response.data;
}

export const estimateRenderPrice = async (rawPrompt, templateId, width=512, height=512) => {
    const response = await axios.get('/v1/estimate_render_price/', {params: {
        raw_prompt: rawPrompt,
        render_template_id: templateId,
        width, height
    }});
    return response.data;
}

