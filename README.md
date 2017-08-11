# intercepteur

        Redirect to the messages handlers added (unlimited). Work with printwmh.py
        It can work with a message handler i made: herms.py if you don't want to develop it.
        For the moment this script is not published becaue all my project was written in another manner, so
        i must rewrite some parts, even if it work actually.

        Intercept a writing signal, work with a message structured like this messHandler::lvlMess::message
        Your message handler must integrate a module named 'feed'

        Note: you can change the '::' separator by what you want.

        To redirect your output messages to this class you need to use in your code:

        myinterceptobj = intercepteur.Intercepteur()
        myinterceptobj.separateur = '::'        # - Note: '::' is present by default, it's just to explain, you can replace it by something else
        myinterceptobj.add_handler = XXX        # - It's an obj you create to manage your messages

        sys.stdout = myinterceptobj

        At this point, it prefix all the messages that don't use a message handler by "unmanaged" to guide you for the transition

        to back in normal mode, use: sys.stdout = sys.__stdout__


        Well, I think it's all... I'm sorry for my bad english, i'm French and made this without translater or help.
    
