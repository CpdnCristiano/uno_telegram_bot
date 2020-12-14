def playBot( player, bot, chat, game, job_queue):
        if len(player.playable_cards()) == 0:
            cards=game.draw_counter or 1
            bot.sendMessage(chat.id, 
            text='Medicilândia uno bot comprou {cards} cartas:'
                .format(cards=cards),
            timeout=TIMEOUT)
            player.draw()
            if len(player.playable_cards()) == 0 or cards > 1:
                game.turn()
                bot.sendMessage(chat.id, 
                text='Medicilândia uno bot passou a vez',
                timeout=TIMEOUT)
            else: 
                cardPla = player.playable_cards()[0]
                player.play(cardPla)
                bot.sendMessage(chat.id, 
                text='Medicilândia uno bot jogou:',
                timeout=TIMEOUT)
                bot.sendSticker(chat.id,
                                sticker=c.STICKERS[str(cardPla)],
                                timeout=TIMEOUT)
                if cardPla.special : 
                    color = c.COLORS[randint(0, 3)]
                    bot.sendMessage(chat.id, 
                    text='Medicilândia escolheu a cor: {selectColor}'
                        .format(selectColor=c.COLOR_ICONS[color]), 
                        timeout=TIMEOUT)
                    game.choose_color(color)
        else: 
            cardPla = player.playable_cards()[0]
            player.play(cardPla)
            bot.sendMessage(chat.id, 
                text='Medicilândia uno bot jogou:',
                timeout=TIMEOUT)
            bot.sendSticker(chat.id,
                                sticker=c.STICKERS[str(cardPla)],
                timeout=TIMEOUT)
            if cardPla.special : 
                color = c.COLORS[randint(0, 3)]
                bot.sendMessage( chat.id, 
                    text='Medicilândia escolheu a cor: {selectColor}'
                        .format(selectColor=c.COLOR_ICONS[color]),
                    timeout=TIMEOUT)
                game.choose_color(color)

        nextplayer_message = ("Next player: {name}"
            .format(name=display_name(game.current_player.user)))
        choice = [[InlineKeyboardButton(text=("Make your choice!"), 
        switch_inline_query_current_chat='')]]
        bot.sendMessage(chat.id,
                        text= nextplayer_message,
                        reply_markup=InlineKeyboardMarkup(choice),
                        timeout=TIMEOUT)

        if game.current_player.user.id == bot.id:
            playBot(player, bot, chat, game, job_queue)