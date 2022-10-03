import { useRef, useState, useEffect } from 'react';

import { styled } from '@mui/material/styles';
import { TextField, Popper, Grow, MenuList, MenuItem, Paper, Button, ButtonGroup } from '@mui/material';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import { getRenderTemplates } from 'src/services/RenderService';
import { useRouter } from 'next/router';

const backupTemplates = [
  {
    "pk": 3,
    "name": "Sản phẩm mẫu",
    "description": "Ảnh chụp cận cảnh các loại sản phẩm"
  },
  {
    "pk": 2,
    "name": "Động vật",
    "description": "Tranh vẽ với chủ thể là các động vật trong tự nhiên"
  },
];


const TemplateButton = styled(Button)(({ theme }) => ({
    // color: theme.palette.getContrastText(purple[500]),
    backgroundColor: theme.palette.grey[700],
    '&:hover': {
      backgroundColor: theme.palette.grey[800],
    },
}));


export const RenderButtonGroup = ({onSubmit, onTemplateChange=() => {}, defaultTemplateId=undefined}) => {
    const anchorRef = useRef(null);
    const [open, setOpen] = useState(false);
    const [selectedTemplate, setSelectedTemplate] = useState(null);
    const [templates, setTemplates] = useState([]);

    const { query } = useRouter();

    useEffect(() => {
        (async () => {
          try {
            const res = await getRenderTemplates();
            setTemplates(res);
          } catch (e) {
            setTemplates(backupTemplates);
          }
        })();
    
      }, [])
    
    useEffect(() => {
        if (!templates || !templates.length) return;

        if (defaultTemplateId === undefined || defaultTemplateId === null) setSelectedTemplate(templates[Math.floor(Math.random() * templates.length)]);
        else {
          for (let i=0; i<templates.length; i++) {
            if (templates[i].pk == defaultTemplateId) {
              setSelectedTemplate(templates[i]); return;
            }
          }

          // choose random template
          setSelectedTemplate(templates[Math.floor(Math.random() * templates.length)]);
        }
    }, [templates, defaultTemplateId])


    const handleToggleTemplateButton = (e) => {
        setOpen((prevOpen) => !prevOpen);
    }

    const handleClose = (e) => {
        if (
        anchorRef.current &&
        anchorRef.current.contains(e.target)
        ) {
        return;
        }

        setOpen(false);
    };

    const handleMenuItemClick = (e, template) => {
        setSelectedTemplate(template);
        setOpen(false);
    }

    return (
      <>
        <ButtonGroup variant="contained" size='large' disableElevation={true}>
            <TemplateButton endIcon={<ArrowDropDownIcon/>} style={{borderRadius: '20px 0 0 20px', whiteSpace: 'nowrap', height: '60px'}} onClick={handleToggleTemplateButton} ref={anchorRef}>
                {selectedTemplate && selectedTemplate.name}
            </TemplateButton>
            <Button
                sx={{borderRadius: '0 20px 20px 0', whiteSpace: 'nowrap', minWidth: '200px', height: '60px'}}
                onClick={() => onSubmit(selectedTemplate.pk)}
            >
                Tạo tranh
            </Button>
        </ButtonGroup>
        <Popper
          sx={{
            zIndex: 1,
          }}
          open={open}
          anchorEl={anchorRef.current}
          role={undefined}
          transition
          disablePortal
        >
          {({ TransitionProps, placement }) => (
            <Grow
              {...TransitionProps}
              style={{
                transformOrigin:
                  placement === 'bottom' ? 'center top' : 'center bottom',
              }}
            >
              <Paper>
                <ClickAwayListener onClickAway={handleClose}>
                  <MenuList id="split-button-menu" autoFocusItem>
                    {templates.map(template => (
                      <MenuItem
                        key={template.pk}
                        selected={template.pk === selectedTemplate.pk}
                        onClick={(event) => handleMenuItemClick(event, template)}
                      >
                        {template.name}
                      </MenuItem>
                    ))}
                  </MenuList>
                </ClickAwayListener>
              </Paper>
            </Grow>
          )}
        </Popper>
      </>
    )
}

