return {
  'nvim-telescope/telescope.nvim',
  event = 'VimEnter',
  dependencies = {
    'nvim-lua/plenary.nvim',
    {
      'nvim-telescope/telescope-fzf-native.nvim',
      build = 'make',
      cond = function()
        return vim.fn.executable('make') == 1
      end,
    },
    { 'nvim-telescope/telescope-ui-select.nvim' },
    { 'nvim-tree/nvim-web-devicons', enabled = vim.g.have_nerd_font },
  },
  config = function()
    local telescope = require("telescope")
    local actions = require("telescope.actions")
    local action_state = require("telescope.actions.state")
    local builtin = require("telescope.builtin")

    telescope.setup({
      extensions = {
        ['ui-select'] = require('telescope.themes').get_dropdown(),
      },
    })

    pcall(telescope.load_extension, 'fzf')
    pcall(telescope.load_extension, 'ui-select')
    pcall(telescope.load_extension, 'todo-comments')
    pcall(telescope.load_extension, 'harpoon')

    -- Markdown Preview Picker
    local function markdown_preview_picker()
      print("✅ Markdown picker loaded")
      builtin.find_files(require("telescope.themes").get_dropdown({
        prompt_title = "🔎 Markdown Preview",
        cwd = vim.fn.expand("~/MyStuff"),
        find_command = { "fd", "--type", "f", "--extension", "md" },
        previewer = false,
        attach_mappings = function(_, map)
          map("i", "<CR>", function(prompt_bufnr)
            local entry = action_state.get_selected_entry()
            actions.close(prompt_bufnr)
            vim.cmd("edit " .. entry.path)
            vim.cmd("MarkdownPreview")
          end)
          return true
        end,
      }))
    end

    -- Keymaps
    vim.keymap.set("n", "<leader>mp", markdown_preview_picker, { desc = "Markdown Preview Picker" })
    vim.keymap.set('n', '<leader>sh', builtin.help_tags, { desc = '[S]earch [H]elp' })
    vim.keymap.set('n', '<leader>sk', builtin.keymaps, { desc = '[S]earch [K]eymaps' })
    vim.keymap.set('n', '<leader>ss', builtin.builtin, { desc = '[S]earch [S]elect Telescope' })
    vim.keymap.set('n', '<leader>sw', builtin.grep_string, { desc = '[S]earch current [W]ord' })
    vim.keymap.set('n', '<leader>sg', builtin.live_grep, { desc = '[S]earch by [G]rep' })
    vim.keymap.set('n', '<leader>sd', builtin.diagnostics, { desc = '[S]earch [D]iagnostics' })
    vim.keymap.set('n', '<leader>sr', builtin.resume, { desc = '[S]earch [R]esume' })
    vim.keymap.set('n', '<leader>s.', builtin.oldfiles, { desc = '[S]earch Recent Files ("." for repeat)' })
    vim.keymap.set("n", "<leader>ts", builtin.treesitter, { desc = "Telescope [T]ree[S]itter Symbols" })
    vim.keymap.set("n", "<leader>bs", builtin.lsp_document_symbols, { desc = "[B]uffer [S]ymbols (LSP)" })
    vim.keymap.set("n", "<leader>fo", "<cmd>Telescope oldfiles<CR>", { desc = "[F]ile [O]ld (Recent Files)" })
    vim.keymap.set("n", "<leader>fw", "<cmd>Telescope live_grep<CR>", { desc = "[F]ind [W]ord (Grep)" })
    vim.keymap.set('n', '<leader><leader>', builtin.buffers, { desc = '[ ] Find existing buffers' })
    vim.keymap.set("n", "<leader>td", function()
      telescope.extensions["todo-comments"].todo({
        cwd = vim.fn.expand("~/.config/nvim/PythonProjects"),
      })
    end, { desc = "List TODOs with Telescope" })

    vim.keymap.set("n", "<leader>tf", function()
      telescope.extensions["todo-comments"].todo({
        keywords = "FIX, FIXME",
        cwd = vim.fn.expand("~/.config/nvim/PythonProjects"),
      })
    end, { desc = "List FIXes with Telescope" })

    vim.keymap.set('n', '<leader>/', function()
      builtin.current_buffer_fuzzy_find(require('telescope.themes').get_dropdown {
        winblend = 10,
        previewer = false,
      })
    end, { desc = '[/] Fuzzily search in current buffer' })

    vim.keymap.set('n', '<leader>s/', function()
      builtin.live_grep {
        grep_open_files = true,
        prompt_title = 'Live Grep in Open Files',
      }
    end, { desc = '[S]earch [/] in Open Files' })

    vim.keymap.set('n', '<leader>sf', function()
      builtin.find_files { cwd = '~/.config/nvim' }
    end, { desc = '[S]earch [F]iles' })

    vim.keymap.set('n', '<leader>sp', function()
      builtin.find_files { cwd = '~/.config/nvim/PythonProjects' }
    end, { desc = '[S]earch [P]ythonProjects' })

    vim.keymap.set('n', '<leader>sv', function()
      builtin.find_files {
        cwd = '~/MyStuff',
        find_command = { 'fd', '--type', 'f', '--extension', 'md' },
      }
    end, { desc = '[S]earch [V]ault (Markdown)' })

    vim.keymap.set('n', '<leader>hh', function()
      builtin.current_buffer_fuzzy_find({
        prompt_title = "Markdown Headings",
        default_text = "#",
      })
    end, { desc = "Headings in Current File" })

    vim.keymap.set('n', '<leader>sn', function()
      builtin.find_files { cwd = vim.fn.stdpath('config') }
    end, { desc = '[S]earch [N]eovim files' })

    vim.keymap.set("n", "<leader>rp", function()
      local file = vim.fn.expand("%:p")
      local Terminal = require("toggleterm.terminal").Terminal

      local py_term = Terminal:new({
        cmd = "python3 " .. file,
        direction = "horizontal",
        size = 15,
        close_on_exit = false,
        start_in_insert = true,
        on_open = function(term)
          vim.cmd("startinsert!")
        end,
      })
      py_term:toggle()
    end, { desc = "Run Python in ToggleTerm" })
  end,
}